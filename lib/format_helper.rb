require File.join(File.dirname(__FILE__),'ip_range.rb')

class FrontendFormatHelper

  @IP_Range

  def initialize(ip_range)
    @IP_Range = ip_range
  end

  def dotted_hash
    hash = @IP_Range.split
    
    if (hash)
      net_string = hash[:net].join unless hash[:net].length == 0
      mixed_string = hash[:mixed].join unless hash[:mixed].length == 0
      host_string = hash[:host].join unless hash[:host].length == 0
    
      #remove_separators(net_string, mixed_string, host_string)
    
      char_count = 0
      insert_count = 0
    
      nl = net_string.length rescue 0
      ml = mixed_string.length rescue 0
      hl = host_string.length rescue 0
    
      while char_count+insert_count <= (nl + ml + hl + insert_count - @IP_Range.size_of_sections)
        char_count = char_count+1
        if (char_count % @IP_Range.size_of_sections == 0)
          insert_in_right_string(net_string, mixed_string, host_string, char_count+insert_count)
          insert_count = insert_count+1
        end
      end
    end
    {:net => net_string, :mixed => mixed_string, :host => host_string}
  end
  
  private
    # insert the separator at the right position in the right string
    # example
    #      net              host
    # |----:----:|-|---:----:----:----|
    #
    def insert_in_right_string(net_string, mixed_string, host_string, count)
      
      nl = net_string.length rescue 0
      ml = mixed_string.length rescue 0
      hl = host_string.length rescue 0
      
      #don't insert at the very end
      # if count >= (nl + ml + hl)
      #   return
      # end

      if count <= nl
        net_string.insert(count,@IP_Range.separator)
      elsif count <= nl + ml
        mixed_string.insert(count - nl, @IP_Range.separator)
      else
        host_string.insert(count - nl - ml, @IP_Range.separator)
      end
    end
end